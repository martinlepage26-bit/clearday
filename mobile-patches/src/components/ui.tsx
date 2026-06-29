/**
 * Shared primitive UI components for Clearday Mobile.
 * Keeps imports simple — import from "@/components/ui".
 */
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
  ActivityIndicator,
  type ViewProps,
  type TextProps,
  type TouchableOpacityProps,
  type TextInputProps,
} from "react-native";

// ─── Card ─────────────────────────────────────────────────────────────────────
export function Card({ className = "", children, ...props }: ViewProps & { className?: string }) {
  return (
    <View className={`bg-white rounded-xl border border-border p-4 ${className}`} {...props}>
      {children}
    </View>
  );
}

export function CardTitle({ className = "", children, ...props }: TextProps & { className?: string }) {
  return (
    <Text className={`text-sm font-semibold text-foreground mb-1 ${className}`} {...props}>
      {children}
    </Text>
  );
}

export function CardDescription({ className = "", children, ...props }: TextProps & { className?: string }) {
  return (
    <Text className={`text-xs text-muted-foreground ${className}`} {...props}>
      {children}
    </Text>
  );
}

// ─── Button ───────────────────────────────────────────────────────────────────
interface ButtonProps extends TouchableOpacityProps {
  variant?: "primary" | "outline" | "ghost" | "destructive";
  size?: "sm" | "md" | "lg";
  className?: string;
  children: React.ReactNode;
}

export function Button({
  variant = "primary",
  size = "md",
  className = "",
  children,
  disabled,
  ...props
}: ButtonProps) {
  const base = "rounded-lg items-center justify-center flex-row gap-1";
  const sizeClass = size === "sm" ? "px-3 py-2 min-h-[36px]" : size === "lg" ? "px-6 py-4 min-h-[52px]" : "px-4 py-3 min-h-[44px]";
  const variantClass =
    variant === "outline"
      ? "border border-primary bg-transparent"
      : variant === "ghost"
      ? "bg-transparent"
      : variant === "destructive"
      ? "bg-destructive"
      : "bg-primary";
  const opacityClass = disabled ? "opacity-50" : "";

  return (
    <TouchableOpacity
      className={`${base} ${sizeClass} ${variantClass} ${opacityClass} ${className}`}
      disabled={disabled}
      activeOpacity={0.75}
      {...props}
    >
      {typeof children === "string" ? (
        <Text
          className={
            variant === "outline"
              ? "text-primary font-medium text-sm"
              : variant === "ghost"
              ? "text-muted-foreground font-medium text-sm"
              : "text-white font-medium text-sm"
          }
        >
          {children}
        </Text>
      ) : (
        children
      )}
    </TouchableOpacity>
  );
}

// ─── Input ────────────────────────────────────────────────────────────────────
export function Input({ className = "", ...props }: TextInputProps & { className?: string }) {
  return (
    <TextInput
      className={`border border-border rounded-lg px-3 py-3 text-sm text-foreground bg-white min-h-[44px] ${className}`}
      placeholderTextColor="#9CA3AF"
      {...props}
    />
  );
}

// ─── Label ────────────────────────────────────────────────────────────────────
export function Label({ className = "", children, ...props }: TextProps & { className?: string }) {
  return (
    <Text className={`text-sm font-medium text-foreground mb-1.5 ${className}`} {...props}>
      {children}
    </Text>
  );
}

// ─── Badge ────────────────────────────────────────────────────────────────────
interface BadgeProps extends ViewProps {
  variant?: "default" | "secondary" | "outline" | "amber";
  className?: string;
  children: React.ReactNode;
}

export function Badge({ variant = "secondary", className = "", children }: BadgeProps) {
  const variantClass =
    variant === "outline"
      ? "border border-border bg-transparent"
      : variant === "amber"
      ? "bg-amber-50 border border-amber-200"
      : variant === "default"
      ? "bg-primary"
      : "bg-muted";

  const textClass =
    variant === "default"
      ? "text-white"
      : variant === "amber"
      ? "text-amber-800"
      : "text-muted-foreground";

  return (
    <View className={`rounded-full px-2 py-0.5 ${variantClass} ${className}`}>
      {typeof children === "string" ? (
        <Text className={`text-xs font-medium ${textClass}`}>{children}</Text>
      ) : (
        children
      )}
    </View>
  );
}

// ─── Skeleton ─────────────────────────────────────────────────────────────────
export function Skeleton({ className = "" }: { className?: string }) {
  return <View className={`bg-muted rounded-lg animate-pulse ${className}`} />;
}

// ─── Spinner ──────────────────────────────────────────────────────────────────
export function Spinner({ size = "small", color = "#2D6A4F" }: { size?: "small" | "large"; color?: string }) {
  return <ActivityIndicator size={size} color={color} />;
}

// ─── Divider ──────────────────────────────────────────────────────────────────
export function Divider({ className = "" }: { className?: string }) {
  return <View className={`h-px bg-border my-3 ${className}`} />;
}

// ─── SafetyBoundary ───────────────────────────────────────────────────────────
export function SafetyBoundary({ text }: { text: string }) {
  return (
    <View className="rounded-lg border border-border bg-muted/50 p-3 mt-2">
      <Text className="text-xs text-muted-foreground leading-relaxed">{text}</Text>
    </View>
  );
}

// ─── SectionHeader ────────────────────────────────────────────────────────────
export function SectionHeader({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <Text className={`text-lg font-semibold text-foreground mb-1 ${className}`}>
      {children}
    </Text>
  );
}

// ─── InfoBanner ───────────────────────────────────────────────────────────────
export function InfoBanner({ children, variant = "info" }: { children: React.ReactNode; variant?: "info" | "amber" | "destructive" }) {
  const bg = variant === "amber" ? "bg-amber-50 border-amber-200" : variant === "destructive" ? "bg-red-50 border-red-200" : "bg-muted border-border";
  const textColor = variant === "amber" ? "text-amber-800" : variant === "destructive" ? "text-red-800" : "text-muted-foreground";
  return (
    <View className={`rounded-lg border p-3 ${bg}`}>
      <Text className={`text-xs leading-relaxed ${textColor}`}>{children}</Text>
    </View>
  );
}

// ─── Chip (category filter) ───────────────────────────────────────────────────
interface ChipProps {
  label: string;
  active?: boolean;
  onPress?: () => void;
  testID?: string;
}
export function Chip({ label, active, onPress, testID }: ChipProps) {
  return (
    <TouchableOpacity
      onPress={onPress}
      testID={testID}
      activeOpacity={0.75}
      className={`px-3 py-1.5 rounded-full border mr-2 mb-2 min-h-[36px] justify-center ${active ? "bg-primary border-primary" : "bg-white border-border"}`}
    >
      <Text className={`text-xs font-medium ${active ? "text-white" : "text-muted-foreground"}`}>
        {label}
      </Text>
    </TouchableOpacity>
  );
}
